#
# Makefile for libRadtran's examples/GUI/spectrum_terrestrial_sbdart directory
#
# Arve Kylling
# arve.kylling@nilu.no

TOPDIR = ../../..

srcdir = .


THISDIR = transmittance_reptran

EXAMPLEFILES = transmittance_reptran_plot.py \
	transmittance_reptran.png \
	transmittance_reptran_prev.jpg transmittance_reptran_info.txt \
	transmittance_reptran_thumb.jpg transmittance_reptran.INP \
	transmittance_reptran.OUT

DISTFILES = Makefile.in $(EXAMPLEFILES)

MYSTICDISTFILES = $(DISTFILES)

include $(TOPDIR)/Makeconf

all: inp.inp big.jpg thumb.jpg info.txt

inp.inp:
	cp transmittance_reptran.INP inp.inp

big.jpg: 
	cp transmittance_reptran_prev.jpg big.jpg

thumb.jpg:
	cp transmittance_reptran_thumb.jpg thumb.jpg

info.txt:
	cp transmittance_reptran_info.txt info.txt

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

