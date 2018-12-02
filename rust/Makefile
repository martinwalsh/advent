include ../.makefiles/ludicrous.mk
include ../.makefiles/docker-compose.mk

export OPTS ?=

#> run unit tests
#>   > make test
#>   > make test OPTS="--test test_name"
test: | build
	$(call log,running tests ($(notdir $(CURDIR))))
	docker-compose run --rm test

#> start the next puzzle
next:
	@:

#> remove build artifacts
clean::
	rm -rf target Cargo.lock

.PHONY: test next clean
