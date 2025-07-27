# Lora E220

## 1. Set up respi-config

Interface Options -> Serial Port

```bash
sudo raspi-config
```

- Would you like a login shell to be accessible over serial? No
- Would you like the serial port hardware to be enabled? Yes

Reboot system

```bash
sudo reboot
```

## 2. Add user to dialout group

```bash
sudo usermod -a -G dialout $USER
```

## 3. Run transmitter.py

```bash
sudo python3 transmitter.py
```
