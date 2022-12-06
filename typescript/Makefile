include ../.makefiles/ludicrous.mk
include ../.makefiles/docker-compose.mk

export OPTS ?=

# NOTE: This forces the container to build everytime, for the purpose of
# updating test config and other scaffolding since the top-level dir is not
# bind mounted to the running container.
build::
	make .docker-compose-build-complete -B

#> run unit tests
#>   > make test
test: | build lint
	$(call log,running tests ($(notdir $(CURDIR))))
	docker-compose run --rm test


#> run the linter on src files
lint: | build
	docker-compose run --rm test yarn lint $(OPTS)

#> run the formatter on src files
format: | build
	docker-compose run --rm test yarn prettier --write ./src/


#> launch a bourne shell in the test environment
shell: | build
	docker-compose run --rm test sh


#> start the next puzzle
next:
	@../.makefiles/next.sh 'src/dayNN.ts'
	@../.makefiles/next.sh 'src/dayNN.test.ts' dayNN


clean::
	rm -rf ./node_modules


.PHONY: test shell next clean lint format
