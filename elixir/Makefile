include ../.makefiles/ludicrous.mk
ADDITIONAL_BUILD_REQS := mix.exs
include ../.makefiles/docker-compose.mk

export OPTS ?=

#> run unit tests
#>   > make test
#>   > make test OPTS="--trace"
test: | build
	$(call log,running tests ($(notdir $(CURDIR))))
	docker-compose run --rm test

shell: | build
	docker-compose run --rm test iex -S mix

#> start the next puzzle
next:
	@../.makefiles/next.sh 'lib/advent/dayNN.ex' dayNN DayNN
	@../.makefiles/next.sh 'test/dayNN_test.exs' dayNN DayNN

clean::
	git clean -fdnX

.PHONY: test shell next clean
