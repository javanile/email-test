
-include .env
export $(shell test -f .env && cut -d= -f1 .env)

test-imap-list:
	@python3 tests/imap-list-test.py
