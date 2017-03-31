# Mausberry Shutdown Circuit

More info on https://mausberry-circuits.myshopify.com/

This replaces the setup.sh and switch.sh scripts of Mausberry. It watches the
shutdown circuit so that when the button is switched to OFF it can shutdown the
machine cleanly.

The big difference between this code and the code from Mausberry is that this
does not run a loop to check the state of the GPIO pin, but uses an interrupt
and thus uses a lot less resources.

## Requirements

Python 3
Python module RPi.GPIO

## Install

```
make install
sudo systemctl daemon-reload
sudo systemctl enable mausberry
```

## Uninstall

```
make uninstall
sudo systemctl daemon-reload
```

## License

MIT license, see the [`LICENSE`](LICENSE) file.
