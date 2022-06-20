####################### Trying with csa & metropolitan_divisions #######################
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
