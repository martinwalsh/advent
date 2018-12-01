include ../.makefiles/ludicrous.mk
include ../.makefiles/docker-compose.mk

export OPTS ?= -v

#> run unit tests
#>   > make test
#>   > make test OPTS=specs/day01_spec.cr
test: | build
	$(call log,running tests ($(notdir $(CURDIR))))
	docker-compose run --rm test

#> start the next puzzle
next:
	@../.makefiles/next.sh 'src/dayNN.cr' DayNN
	@../.makefiles/next.sh 'spec/dayNN_spec.cr' dayNN DayNN

.PHONY: test
