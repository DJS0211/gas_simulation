#
# Makefile for libRadtran's example/<subdir> directory
#

TOPDIR = ../..

srcdir = .


THISDIR = $(notdir $(CURDIR))

SUBDIRS =

EXAMPLEFILES = \
	$(wildcard *.DAT) \
	$(wildcard *.INP) \
	$(wildcard *.OUT) \

DISTFILES = Makefile.in $(EXAMPLEFILES)

include $(TOPDIR)/Makeconf

all:
	for dir in $(SUBDIRS); do $(MAKE) -C $$dir $@ || exit $$?; done
.PHONY: all

dist: all
	for dir in $(SUBDIRS); do mkdir $(TOPDIR)/`cat $(TOPDIR)/.fname`/examples/$(THISDIR)/$$dir; $(MAKE) -C $$dir $@ || exit $$?; done; \
	ln $(DISTFILES) $(TOPDIR)/`cat $(TOPDIR)/.fname`/examples/$(THISDIR)
.PHONY: dist

mystic-dist: dist
.PHONY: mystic-dist

install: all
	$(MKPATH) $(examplesdir)/$(THISDIR)
	$(INSTALL_DATA) $(EXAMPLEFILES) $(examplesdir)/$(THISDIR)
.PHONY: install

clean:
	rm -f MC*.EDN MC*.EUP MC*.HEAT MC.OUT.* mc.* randomseed plot_hr.py hr.pdf dummy
.PHONY: clean

mostlyclean: clean
.PHONY: mostlyclean

distclean: mostlyclean
	rm -f Makefile
.PHONY: distclean

realclean: distclean
	rm -f *.DAT DISORT* MC*
.PHONY: realclean

Makefile: Makefile.in $(TOPDIR)/config.status
	cd $(TOPDIR); sh config.status

gen_test_files: gen_test_files.sh
	bash gen_test_files.sh --dry
.PHONY: gen_test_files
