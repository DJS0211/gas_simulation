#
# Makefile for libRadtran's examples/GUI/spectrum_GOME directory
#
# Arve Kylling
# arve.kylling@nilu.no

TOPDIR = ../../..

srcdir = .


THISDIR = spectrum_GOME

EXAMPLEFILES =   \
	spectrum_GOME_info.txt spectrum_GOME.inp  spectrum_GOME.out \
	spectrum_GOME_prev.jpg spectrum_GOME_thumb.jpg \
	spectrum_GOME_plot.py  spectrum_GOME.png \
	solar_file

DISTFILES = Makefile.in $(EXAMPLEFILES)

MYSTICDISTFILES = $(DISTFILES)

include $(TOPDIR)/Makeconf

all: inp.inp big.jpg thumb.jpg info.txt

inp.inp:
	cp spectrum_GOME.inp inp.inp

big.jpg: 
	cp spectrum_GOME_prev.jpg big.jpg

thumb.jpg:
	cp spectrum_GOME_thumb.jpg thumb.jpg

info.txt:
	cp spectrum_GOME_info.txt info.txt

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

