SRC=mausberry.py
DST=/usr/sbin/mausberry

SERVICE_SRC=mausberry.service
SERVICE_DST=/etc/systemd/system/$(SERVICE_SRC)

.PHONY=all install uninstall

all:
	@echo "Install using:"
	@echo "  make install"

install: $(SRC)
	sudo cp $(SRC) $(DST)
	sudo cp $(SERVICE_SRC) $(SERVICE_DST)
	sudo chown root:root $(DST) $(SERVICE_DST)
	sudo chmod 700 $(DST)
	sudo chmod 644 $(SERVICE_DST)
	@echo "Don't forget to run:"
	@echo "  systemctl daemon-reload"
	@echo "  systemctl enable mausberry"

uninstall:
	sudo rm -f $(DST) $(SERVICE_DST)
	@echo "Don't forget to run:"
	@echo "  systemctl daemon-reload"
