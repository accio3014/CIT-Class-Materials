cwd=$(cd "$( dirname "${BASH_SOURCE[0]}")" && pwd)

if hash pip3 2>/dev/null; then
  sudo pip3 install $cwd/py3minepi-master
else
  sudo pip install $cwd/py3minepi-master
fi
