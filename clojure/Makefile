include ../.makefiles/ludicrous.mk
include ../.makefiles/docker-compose.mk

export OPTS ?=

#> run unit tests
#>   > make test
#>   > make test OPTS=CHANGEME
test: | build
	$(call log,running tests ($(notdir $(CURDIR))))
	docker-compose run --rm test

shell: | build
	docker-compose run --rm test lein repl

#> start the next puzzle
next:
	@../.makefiles/next.sh 'src/dayNN.clj' dayNN
	@../.makefiles/next.sh 'test/dayNN_test.clj' dayNN

clean::
	rm -rf target/ .lein-failures .lein-repl-history

Dockerfile: # Required by the shared docker-compose targets (no-op).
	@:

.PHONY: test shell next Dockerfile
