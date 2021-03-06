PELICAN       ?= pelican
PELICANOPTS    =
PORT           = 8000

BASEDIR	       = $(CURDIR)
INPUTDIR       = $(BASEDIR)/content
OUTPUTDIR      = $(BASEDIR)/output
CONFFILE       = $(BASEDIR)/pelican/conf.py
PUBLISHCONF    = $(BASEDIR)/pelican/conf_pub.py
DEVSERVER      = $(BASEDIR)/pelican/devserver
REDIRS         = $(BASEDIR)/pelican/redir.cfg

# for server-helper
export PELICAN PELICANOPTS BASEDIR INPUTDIR OUTPUTDIR CONFFILE
export DEVSERVER REDIRS PORT

SERVER_HELPER  = $(BASEDIR)/pelican/server-helper

SSH_HOST       = of-readings
SSH_PORT       = 22
SSH_USER       =
SSH_TARGET_DIR = html/

ifeq ($(SSH_USER),)
SSH_DESTINATION :=             $(SSH_HOST):$(SSH_TARGET_DIR)
else
SSH_DESTINATION := $(SSH_USER)@$(SSH_HOST):$(SSH_TARGET_DIR)
endif

DEBUG ?= 0
ifeq ($(DEBUG),1)
	PELICANOPTS += -D
endif

define help_message
Makefile for a pelican Web site

Usage:
   make html                        (re)generate the web site
   make publish                     generate using production settings
   make clean                       remove the generated files
   make regenerate                  regenerate files upon modification
   make serve [PORT=8000]           serve site at http://localhost:8000
   make devserver [PORT=8000]       serve site and regenerate files
   make stopserver                  stop local servers
   make ssh_upload                  upload the web site via SSH
   make rsync_upload                upload the web site via rsync+ssh

Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html
endef

help:
	$(file >/dev/stdout,$(help_message))

html:
	mkdir -p $(OUTPUTDIR)
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

clean:
	-rm -rf $(OUTPUTDIR) $(BASEDIR)/pelican/cache

regenerate:
	mkdir -p $(OUTPUTDIR)
	$(SERVER_HELPER) restart pelican

serve: html
	$(SERVER_HELPER) restart http

devserver:
	mkdir -p $(OUTPUTDIR)
	$(SERVER_HELPER) restart

stopserver:
	$(SERVER_HELPER) stop

publish:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

rsync_upload: publish
	rsync -e "ssh -p $(SSH_PORT)" -P -rvzc --delete \
	    --cvs-exclude --exclude /comments/ --exclude /.htaccess.gz \
	    --exclude /s/.webassets-cache/ \
	    $(OUTPUTDIR)/ $(SSH_DESTINATION)/

.PHONY: html help clean regenerate serve devserver publish \
        ssh_upload rsync_upload
