import pytest

from io import StringIO
from django.core.management import call_command

from users.models import User


@pytest.mark.django_db
class TestUserManager:
    def test_create_user(self):
        user = User.objects.create_user(
            email="john@example.com",
            password="something-r@nd0m!",
        )

        assert user.email == "john@example.com"
        assert not user.is_staff
        assert not user.is_superuser
        assert user.check_password("something-r@nd0m!")
        assert user.username is None

    def test_create_superuser(self):
        user = User.objects.create_superuser(
            email="admin@example.com",
            password="something-r@nd0m!",
        )

        assert user.email == "admin@example.com"
        assert user.is_staff
        assert user.is_superuser
        assert user.username is None

    def test_create_superuser_username_ignored(self):
        user = User.objects.create_superuser(
            email="test@example.com",
            password="something-r@nd0m!",
        )

        assert user.username is None


@pytest.mark.django_db
def test_createsuperuser_command():
    out = StringIO()
    command_result = call_command(
        "createsuperuser",
        "--email",
        "john@example.com",
        interactive=False,
        stdout=out,
    )

    assert command_result is None
    assert out.getvalue() == "Superuser created successfully.\n"
    user = User.objects.get(email="john@example.com")

    assert not user.has_usable_password()
