export STORE_TEST_RESULTS=true
meltano invoke dbt deps

meltano invoke dbt run --select elementary

#  disable pipeline fail on non 0 exit code for dbt test
# save exit code
# re-enable pipeline fail on non 0 exit code
set +e
meltano invoke dbt test --store-failures