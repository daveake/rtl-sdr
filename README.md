rtl-sdr
turns your Realtek RTL2832 based DVB dongle into a SDR receiver
======================================================================

For more information see:
http://sdr.osmocom.org/trac/wiki/rtl-sdr

** Modified to add UDP frequency control of RTL_FM program **

Installation Instructions
=========================

sudo apt-get install git cmake libusb-1.0-0-dev

cd ~

git clone https://github.com/daveake/rtl-sdr.git

cd rtl-sdr

mkdir build

cd build

cmake ../ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON

make

sudo make install

sudo ldconfig

