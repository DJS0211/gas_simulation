#
# Makefile for libRadtran's examples/GUI/spectrum_terrestrial_sbdart directory
#
# Arve Kylling
# arve.kylling@nilu.no

TOPDIR = ../../..

srcdir = .


THISDIR = radiance_sentinel_sunglint

EXAMPLEFILES = radiance_sentinel_sunglint_plot.py \
	radiance_sentinel_sunglint.png  \
	radiance_sentinel_sunglint_prev.jpg radiance_sentinel_sunglint_info.txt \
	radiance_sentinel_sunglint_thumb.jpg radiance_sentinel_sunglint.INP \
        radiance_sentinel_sunglint.OUT

DISTFILES = Makefile.in $(EXAMPLEFILES)

MYSTICDISTFILES = $(DISTFILES)

include $(TOPDIR)/Makeconf

all: inp.inp big.jpg thumb.jpg info.txt

inp.inp:
	cp radiance_sentinel_sunglint.INP inp.inp

big.jpg: 
	cp radiance_sentinel_sunglint_prev.jpg big.jpg

thumb.jpg:
	cp radiance_sentinel_sunglint_thumb.jpg thumb.jpg	

info.txt:
	cp radiance_sentinel_sunglint_info.txt info.txt

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

