include ../.makefiles/ludicrous.mk
include ../.makefiles/docker-compose.mk

export OPTS ?=

#> run unit tests
#>   > make test
#>   > make test OPTS=--stacktrace
test: | build
	$(call log,running tests ($(notdir $(CURDIR))))
	docker-compose run --rm test

#> start the next puzzle
next:
	@../.makefiles/next.sh 'src/main/groovy/adventofcode/DayNN.groovy' dayNN DayNN
	@../.makefiles/next.sh 'src/test/groovy/adventofcode/DayNNTest.groovy' dayNN DayNN

#> remove build artifacts
clean::
	rm -rf .gradle build .java

.PHONY: test next clean
