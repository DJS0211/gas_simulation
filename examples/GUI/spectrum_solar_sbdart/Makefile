#
# Makefile for libRadtran's examples/GUI/spectrum_solar_sbdart directory
#
# Arve Kylling
# arve.kylling@nilu.no

TOPDIR = ../../..

srcdir = .


THISDIR = spectrum_solar_sbdart

EXAMPLEFILES = spectrum_solar_sbdart_plot.py spectrum_solar_sbdart.png \
	spectrum_solar_sbdart_info.txt  spectrum_solar_sbdart_prev.jpg \
	spectrum_solar_sbdart.INP       spectrum_solar_sbdart_prev.png \
	spectrum_solar_sbdart.OUT       spectrum_solar_sbdart_thumb.jpg 

DISTFILES = Makefile.in $(EXAMPLEFILES)

MYSTICDISTFILES = $(DISTFILES)

include $(TOPDIR)/Makeconf

all: inp.inp big.jpg thumb.jpg info.txt

inp.inp:
	cp spectrum_solar_sbdart.INP inp.inp

big.jpg: 
	cp spectrum_solar_sbdart_prev.jpg big.jpg

thumb.jpg:
	cp spectrum_solar_sbdart_thumb.jpg thumb.jpg	

info.txt:
	cp spectrum_solar_sbdart_info.txt info.txt

dist: all
	ln $(DISTFILES) ../../../`cat ../../../.fname`/examples/GUI/$(THISDIR)
.PHONY: dist

mystic-dist: all
	ln $(MYSTICDISTFILES) ../../../`cat ../../../.fname`/examples/GUI/$(THISDIR)
.PHONY: mystic-dist

install: all
	$(MKPATH) $(examplesdir)/GUI/$(THISDIR)
	$(INSTALL_DATA) $(EXAMPLEFILES) $(examplesdir)/GUI/$(THISDIR)
.PHONY: install

clean:

mostlyclean: clean

distclean: clean
	rm -f Makefile config.status

realclean: distclean

Makefile: Makefile.in ../../../config.status
	cd ../../../; sh config.status

# Prevent GNU make v3 from overflowing arg limit on SysV.
.NOEXPORT:

# eof

