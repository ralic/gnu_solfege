#!/bin/bash
set -e

if [ "$OSTYPE" = "msys" ]; then
	export GIT=C:/Programfiler/Git/bin/git.exe
	export GIT="C:/Program Files/Git/bin/git.exe"
	export PYTHON=/c/python34/python.exe
	aclocal-1.11
	autoconf
	configure
	$PYTHON -c "import tools.buildutil; tools.buildutil.create_versions_file('$GIT')"
else
	aclocal $ACINCLUDE
	autoconf
        python3 -c "import tools.buildutil; tools.buildutil.create_versions_file('git')"
fi
