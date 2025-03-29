# Copyright (c) 2025 Lunatic Fringers
#
# This file is part of Shepherd Core Stack
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from typing import override

from service import Service


class DatabaseService(Service):
    @override
    def build_image(self):
        """Build the DBMS image."""
        pass

    @override
    def bootstrap(self):
        """Bootstrap the DBMS service."""
        pass

    @override
    def start(self):
        """Start the DBMS service."""
        pass

    @override
    def halt(self):
        """Halt the DBMS service."""
        pass

    @override
    def reload(self):
        """Reload the DBMS service."""
        pass

    @override
    def show_stdout(self):
        """Show the DBMS stdout."""
        pass

    @override
    def get_shell(self):
        """Get a shell session for the DBMS."""
        pass

    def get_sql_shell(self):
        """Get a SQL shell session."""
        pass

    def create_user(self, user: str, psw: str):
        """Create a new database user."""
        pass

    def create_directory(self, user: str, directory_name: str):
        """Create a directory object in the database."""
        pass

    def remove_user(self, user: str):
        """Drop an existing database user."""
        pass


class DatabaseMng:
    def build_image(self):
        """Build a DBMS image."""
        pass

    def bootstrap(self):
        """Bootstrap a DBMS service."""
        pass

    def start(self):
        """Start a DBMS service."""
        pass

    def halt(self):
        """Halt a DBMS service."""
        pass

    def stdout(self):
        """Show a DBMS stdout."""
        pass

    def shell(self):
        """Get a DBMS shell session."""
        pass

    def sql_shell(self):
        """Get a SQL shell session."""
        pass

    def create_database_user(self, user: str, psw: str):
        """Create a new database user."""
        pass

    def create_database_directory(self, user: str, directory_name: str):
        """Create a directory object in a database."""
        pass

    def remove_database_user(self, user: str):
        """Drop an existing user."""
        pass
