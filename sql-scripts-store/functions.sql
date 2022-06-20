# SQL - BIGQUERY

# REFERENCE MATERIALS
# https://codingisforlosers.com/learn-bigquery-sql/
# https://medium.com/firebase-developers/using-the-unnest-function-in-bigquery-to-analyze-event-parameters-in-analytics-fb828f890b42
# https://www.youtube.com/watch?v=Ww71knvhQ-s, https://www.youtube.com/watch?v=zAmJPdZu8Rg
# SAMPLE EMPLOYEE DATASET USED: https://eforexcel.com/wp/downloads-16-sample-csv-files-data-sets-for-testing/

# TOPIC 1 | FILTERING DATA WITH "WHERE" CLAUSE

select distinct year from `bigquery-public-data.baseball.games_post_wide` limit 5;
select distinct venueName from `bigquery-public-data.baseball.games_post_wide` limit 5;
# Dodger Stadium, Citi Field, Globe Life Park in Arlington, Progressive Field, Wrigley Field
select * from `bigquery-public-data.baseball.games_post_wide` limit 5;

SELECT venueName, startTime, hitterFirstName, homeFinalRuns, homeFinalHits, awayFinalHits,
      hitterWeight, hitterHeight from `bigquery-public-data.baseball.games_post_wide`
      limit 50;

SELECT venueName, startTime, hitterFirstName, homeFinalRuns, homeFinalHits, awayFinalHits,
      hitterWeight, hitterHeight from `bigquery-public-data.baseball.games_post_wide`
      where hitterfirstname = 'Miguel'
limit 5;

SELECT venueName, startTime, hitterFirstName, homeFinalRuns, homeFinalHits, awayFinalHits,
      hitterWeight, hitterHeight from `bigquery-public-data.baseball.games_post_wide`
      where hitterfirstname = 'Christopher' or hitterFirstName = 'Richard'
limit 10;

SELECT venueName, startTime, hitterFirstName, homeFinalRuns, homeFinalHits, awayFinalHits,
      hitterWeight, hitterHeight from `bigquery-public-data.baseball.games_post_wide`
      where hitterfirstname in('Christopher', 'Miguel')
limit 10;

SELECT venueName, startTime, hitterFirstName, homeFinalRuns, homeFinalHits, awayFinalHits,
      hitterWeight, hitterHeight from `bigquery-public-data.baseball.games_post_wide`
      where venuename = 'Dodger Stadium' and hitterFirstName = 'Christopher'
limit 10;

# TOPIC 2 | ORDERING RESULTS WITH "ORDER BY" CLAUSE

SELECT venueName, startTime, hitterFirstName, homeFinalRuns, homeFinalHits, awayFinalHits,
      hitterWeight, hitterHeight from `bigquery-public-data.baseball.games_post_wide`
      where hitterfirstname in('Christopher', 'Miguel')
      order by venuename asc
limit 10;

SELECT venueName, startTime, hitterFirstName, homeFinalRuns, homeFinalHits, awayFinalHits,
      hitterWeight, hitterHeight from `bigquery-public-data.baseball.games_post_wide`
      where hitterfirstname in('Christopher', 'Miguel')
      order by venuename desc
limit 10;


# TOPIC 3 | CALCULATE AGGREGATE TOTALS WITH "GROUP BY"
SELECT venueName,
      sum(homefinalhits) as finalhits, sum(awayfinalhits) as homehits
      from `bigquery-public-data.baseball.games_post_wide`
      where hitterfirstname in('Christopher', 'Miguel')
      group by venuename
      order by venuename asc
      limit 10;

# All the number of columns to be viewed should also be (mentioned in group by) grouped.
SELECT venueName, awayfinalhits,
      sum(homefinalhits) as hits, sum(awayfinalhits) as homehits
      from `bigquery-public-data.baseball.games_post_wide`
      where hitterfirstname in('Christopher', 'Miguel')
      group by venuename, awayfinalhits
      order by venuename asc
      limit 10;

SELECT venueName, awayfinalhits,
      sum(homefinalhits) as hits,
      max(homefinalhits) as maxhits,
      sum(awayfinalhits) as homehits,
      min(awayfinalhits) as minawayhits,
      count(venuename) as noofvenues
      from `bigquery-public-data.baseball.games_post_wide`
      where hitterfirstname in('Christopher', 'Miguel')
      group by venuename, awayfinalhits
      order by venuename asc
      limit 10;

# TOPIC 4 | WRITING ARITHMETIC WITHIN QUERIES with CASE STATEMENTS
# Arithmetics within Queries
SELECT venueName, awayfinalhits,
      sum(homefinalhits) + sum(homefinalhits) as hits_plus_hits,
      max(homefinalhits) * 3 as hits_times_3,
      sum(awayfinalhits) / sum(homefinalhits) as awayhits_over_homehits,
      min(awayfinalhits) - sum(awayfinalhits) as awayhits_minus_awayhits,
      count(venuename) as noofvenues
      from `bigquery-public-data.baseball.games_post_wide`
      where hitterfirstname in('Christopher', 'Miguel')
      group by venuename, awayfinalhits
      order by venuename asc
      limit 10;
# Case Statements. (Case is like if else condition in SQL)
# SYNTAX of case

# CASE WHEN <condition/ statement>
# THEN <condition/ statement>
# ELSE <condition/ statement>
# END (ends the case)

SELECT venueName, awayfinalhits,
      sum(homefinalhits) + sum(homefinalhits) as hits_plus_hits,
      max(homefinalhits) * 3 as hits_times_3,

      CASE WHEN sum(homefinalhits) > 0              # Creating a condition to check denominator "homefinalhits" is not 0
      THEN sum(awayfinalhits) / sum(homefinalhits)  # If 0, execute this process
      ELSE 0                                        # Else keep it as 0. (do not apply any operation)
      END AS finalhits_on_homehits,                 # Creating an alias name for the column.

      from `bigquery-public-data.baseball.games_post_wide`
      where hitterfirstname in('Christopher', 'Miguel')
      group by venuename, awayfinalhits
      order by venuename asc
      limit 10;

# TOPIC 5 | EXTRACT & FORMAT_DATE - DATE, WEEK & MONTH
SELECT venueName, startTime, hitterFirstName, homeFinalRuns, homeFinalHits, awayFinalHits,
      hitterWeight, hitterHeight from `bigquery-public-data.baseball.games_post_wide`
      limit 50;

SELECT startTime,
      EXTRACT(day from startTime) as day,
      EXTRACT(week from startTime) as week,
      EXTRACT(year from starttime) as year,
      FORMAT_DATE("%Y-%m", starttime) as yyymm
      FROM `bigquery-public-data.baseball.games_post_wide`
      limit 50;

# Parse_date/ Parse_datetime is used to convert string type date - to date data type.
#SELECT parse_date('%Y%m%d', startTime) date
#from `bigquery-public-data.baseball.games_post_wide` limit 5;

# TOPIC 6 | NESTING QUERIES
SELECT venueName, startTime, hitterFirstName
      from `bigquery-public-data.baseball.games_post_wide`
      where hitterFirstName = 'Miguel'
      limit 10;

SELECT startTime, hitterfirstname,
      EXTRACT(day from startTime) as day,
      EXTRACT(week from startTime) as week,
      EXTRACT(year from starttime) as year,
      FORMAT_DATE("%Y-%m", starttime) as yyymm
      FROM (SELECT venueName, startTime, hitterFirstName
            from `bigquery-public-data.baseball.games_post_wide`
            where hitterfirstname = 'Miguel')
      limit 50;

# TOPIC 7 | UNNESTING RECORD ARRAYS, ANY_VALUE
# REFERENCE
# https://medium.com/firebase-developers/using-the-unnest-function-in-bigquery-to-analyze-event-parameters-in-analytics-fb828f890b42

SELECT
ANY_VALUE(fruit) as any_value
FROM UNNEST(["apple", "banana", "pear"]) as fruit;
# Unnest is used to unpack values from an array/ list.
# Any_value is used to pick any one value out of a list of elements.

SELECT event_date, event_timestamp, event_name, event_params
FROM `firebase-public-project.analytics_153293282.events_20180915`
LIMIT 5;

# UNNEST Example from a nested column.
SELECT event_date, event_timestamp, event_name, params, event_params
FROM `firebase-public-project.analytics_153293282.events_20180915`
CROSS JOIN                            # Joining the column back to the same table.
UNNEST(event_params) as params        # Unnesting the column which has array & creating a new column
LIMIT 50;


# Same Query above can also be written by replacing 'Cross Join' with a ',' comma.
SELECT event_date, event_timestamp, event_name, params, event_params
FROM `firebase-public-project.analytics_153293282.events_20180915`, # Joining the column back to the same table.
UNNEST(event_params) as params       # Unnesting the column which has array & creating a new column
LIMIT 5;


# Extracted value from a list of dictionaries.
SELECT event_name, params.key, params, params.value.int_value AS score, event_params # .key, .value to fetch dictionary data
FROM `firebase-public-project.analytics_153293282.events_20180915`, # , comma for cross join
UNNEST(event_params) AS params                                      # Unnesting arrays/list
WHERE event_name = "level_complete_quickplay"                       # Specifying which column
AND params.key = "value"                                            # params has multiple keys, specifying which key it is.
LIMIT 5;


SELECT event_name, param.value.int_value AS score
FROM `firebase-public-project.analytics_153293282.events_20180915`,
UNNEST(event_params) AS param
WHERE event_name = "level_complete_quickplay"
AND param.key = "value"
limit 5;

# AVERAGE | APPROX_QUANTILE | STDDEV FUNCTIONS
SELECT AVG(param.value.int_value) AS average,
  APPROX_QUANTILES(param.value.int_value, 2) AS quantiles,
  STDDEV(param.value.int_value) AS stddev
FROM `firebase-public-project.analytics_153293282.events_20180915`,
UNNEST(event_params) AS param
WHERE event_name = "level_complete_quickplay"
AND param.key = "value";


# TOPIC 8 | JOINING TABLES (already written)

# Sample tables considered.
select csa_code, geo_id, name, lsad_name, msa_lsad_code
      from `bigquery-public-data.geo_us_boundaries.csa`; #175 actual records

select csa_code, geo_id, name, lsad_name, cbsa_code, metdiv_code
      from `bigquery-public-data.geo_us_boundaries.metropolitan_divisions`; #31 actual records

# Inner Join - 31 joined records
select csa.csa_code, met.csa_code, csa.geo_id, met.geo_id,
      csa.name, met.name, csa.lsad_name, met.lsad_name
      from `bigquery-public-data.geo_us_boundaries.csa` csa
      inner join `bigquery-public-data.geo_us_boundaries.metropolitan_divisions` met
      on csa.csa_code = met.csa_code;
# Only matching records in both table appear
# If either of the table had multiple records for the matched value, it creates mutiple entries.

# Left Join - 195 joined records
select csa.csa_code, met.csa_code, csa.geo_id, met.geo_id,
      csa.name, met.name, csa.lsad_name, met.lsad_name
      from `bigquery-public-data.geo_us_boundaries.csa` csa
      left join `bigquery-public-data.geo_us_boundaries.metropolitan_divisions` met
      on csa.csa_code = met.csa_code;

# All records in left remain & Only matched records on the right is joined.
# All Unmatched records on right table is marked null.
# If right table has multiple records for the matched value, it creates multiple entries.

# Right Join - 31 records
select csa.csa_code, met.csa_code, csa.geo_id, met.geo_id,
      csa.name, met.name, csa.lsad_name, met.lsad_name
      from `bigquery-public-data.geo_us_boundaries.csa` csa
      right join `bigquery-public-data.geo_us_boundaries.metropolitan_divisions` met
      on csa.csa_code = met.csa_code;
# All records in the right remain & Only matched records on the left is joined.
# If left table has multiple records for the matched value, it creates multiple entries.

# Outer/ Full Join
select csa.csa_code, met.csa_code, csa.geo_id, met.geo_id,
      csa.name, met.name, csa.lsad_name, met.lsad_name
      from `bigquery-public-data.geo_us_boundaries.csa` csa
      full outer join `bigquery-public-data.geo_us_boundaries.metropolitan_divisions` met
      on csa.csa_code = met.csa_code;
# All records in both table remain.
# If left or right table has multiple records for the matched value, it creates multiple entries.

# Cartesian Join
select csa.csa_code, met.csa_code,
      # csa.geo_id, met.geo_id,
      #csa.name, met.name, csa.lsad_name, met.lsad_name
      from `bigquery-public-data.geo_us_boundaries.csa` csa
      cross join `bigquery-public-data.geo_us_boundaries.metropolitan_divisions` met;
# output rows = left table row * right table row (175*31=5425).
# each row in left table is combined with all rows in right.

SELECT a.ROLL_NO , b.NAME
FROM Student a, Student b
WHERE a.ROLL_NO < b.ROLL_NO;
#Self Join
select csa.geo_id, csa_b.geo_id, csa.name, csa_b.name
      from `bigquery-public-data.geo_us_boundaries.csa` csa,
           `bigquery-public-data.geo_us_boundaries.csa` csa_b
      where csa.geo_id = csa_b.geo_id;
# Creates 2 tables from the same table, applies condition to view the columns.

# Self Join - 2: 15225 records
select csa.geo_id, csa_b.geo_id, csa.name, csa_b.name
      from `bigquery-public-data.geo_us_boundaries.csa` csa,
           `bigquery-public-data.geo_us_boundaries.csa` csa_b
      where csa.geo_id > csa_b.geo_id;


# TOPIC 9 | "WITH" STATEMENTS IN BQ SQL
select csa.csa_code, met.csa_code, csa.geo_id, met.geo_id,
      csa.name, met.name, csa.lsad_name, met.lsad_name
      from `bigquery-public-data.geo_us_boundaries.csa` csa
      inner join `bigquery-public-data.geo_us_boundaries.metropolitan_divisions` met
      on csa.csa_code = met.csa_code;

WITH csa as (
      select csa_code, geo_id, name, lsad_name from `bigquery-public-data.geo_us_boundaries.csa`),
     met as (
      select csa_code, geo_id, name, lsad_name from `bigquery-public-data.geo_us_boundaries.metropolitan_divisions`)
SELECT csa.csa_code, met.csa_code, csa.geo_id, met.geo_id,
      csa.name, met.name, csa.lsad_name, met.lsad_name
      from csa
      inner join met
      on csa.csa_code = met.csa_code;

# TOPIC 10 | WINDOW ANALYTIC FUNCTIONS
select * from `searce-practice-data-analytics.viknesh.employee` limit 5;

select emp_id, first_name, county, state, salary
from `searce-practice-data-analytics.viknesh.employee` limit 5;

select county, max(salary) as max_salary
from `searce-practice-data-analytics.viknesh.employee`
group by county
limit 5; # cannot view other columns. can be done using window function.


select emp_id, first_name, county, salary,
max(salary) over() as max_salary  # Over indicates it is a window function
from `searce-practice-data-analytics.viknesh.employee`
limit 5;      # Creates window for all columns


select emp_id, first_name, place_name, salary,
max(salary) over(partition by place_name) as max_salary  # partition creates window(groups) only on the specified column
from `searce-practice-data-analytics.viknesh.employee`
limit 30;

select emp_id, first_name, place_name, salary,
row_number() over() as row_num
from `searce-practice-data-analytics.viknesh.employee`
limit 30;

select emp_id, first_name, place_name, salary,
row_number() over(partition by place_name) as row_num
from `searce-practice-data-analytics.viknesh.employee`
limit 30;


select emp_id, first_name, place_name, salary,
row_number() over(partition by place_name order by emp_id) as row_num
from `searce-practice-data-analytics.viknesh.employee`
limit 30;

# First 2 employees from each place.
select * from(
      select emp_id, first_name, State, salary,
      row_number() over(partition by place_name order by emp_id) as row_num
      from `searce-practice-data-analytics.viknesh.employee`
      limit 30) as sub_table
where sub_table.row_num < 3;

# Fetch the top 5 employees in each place earning the max salary
Select emp_id, first_name, county, salary,
rank() over(partition by county order by salary desc) as rnk
from `searce-practice-data-analytics.viknesh.employee`
limit 1000;

select * from(
      Select emp_id, first_name, county, salary,
      rank() over(partition by county order by salary desc) as rnk
      from `searce-practice-data-analytics.viknesh.employee`) as ranking
where ranking.rnk < 6
limit 1000;

Select emp_id, first_name, county, salary,
rank() over(partition by county order by salary desc) as rnk,
dense_rank() over(partition by county order by salary desc) dense_rnk,
from `searce-practice-data-analytics.viknesh.employee`
limit 1000;

select emp_id, first_name, county, salary,
lag(salary) over(partition by county order by emp_id desc) as previous_emp_sal,
from `searce-practice-data-analytics.viknesh.employee`
limit 50;

select emp_id, first_name, county, salary,
lag(salary, 2, 0) over(partition by county order by emp_id desc) as previous_emp_sal,
from `searce-practice-data-analytics.viknesh.employee`
limit 50;

select emp_id, first_name, county, salary,
lag(salary) over(partition by county order by emp_id desc) as previous_emp_sal,
lead(salary) over(partition by county order by emp_id desc) as next_emp_sal,
from `searce-practice-data-analytics.viknesh.employee`
limit 50;

select emp_id, first_name, county, salary,
lag(salary) over(partition by county order by emp_id) as previous_emp_sal,
case when e.salary > lag(salary) over (partition by county order by emp_id) then 'Higher than previous employee'
     when e.salary < lag(salary) over (partition by county order by emp_id) then 'Lower than previous employee'
     when e.salary = lag(salary) over (partition by county order by emp_id) then 'Same as the previous employee'
     end sal_range
from `searce-practice-data-analytics.viknesh.employee` as e
limit 100;

# TOPIC 12 | DEDUPING QUERY RESULTS
select * #emp_id, first_name, county, Quarter_of_Joining, salary
from `searce-practice-data-analytics.viknesh.employee`
limit 50;

select * from(
select emp_id, first_name, county, Date_of_Birth,
first_value(Date_of_Birth) over(partition by county order by (Date_of_Birth) asc) as first_dob
from `searce-practice-data-analytics.viknesh.employee`
limit 50)
where Date_of_Birth = first_dob;

