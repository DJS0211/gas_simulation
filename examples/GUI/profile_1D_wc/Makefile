#
# Makefile for libRadtran's examples/GUI/profile_1D_wc directory
#
# Arve Kylling
# arve.kylling@nilu.no

TOPDIR = ../../..

srcdir = .


THISDIR = profile_1D_wc

EXAMPLEFILES = info.txt \
	profile_1D_wc_info.txt profile_1D_wc.INP \
	profile_1D_wc.OUT profile_1D_wc_plot.py \
	profile_1D_wc.png \
	profile_1D_wc_prev.jpg profile_1D_wc_thumb.jpg

DISTFILES = Makefile.in $(EXAMPLEFILES)

MYSTICDISTFILES = $(DISTFILES)

include $(TOPDIR)/Makeconf

all: inp.inp big.jpg thumb.jpg info.txt

inp.inp:
	cp profile_1D_wc.INP inp.inp

big.jpg: 
	cp profile_1D_wc_prev.jpg big.jpg

thumb.jpg:
	cp profile_1D_wc_thumb.jpg thumb.jpg	

info.txt:
	cp profile_1D_wc_info.txt info.txt

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

