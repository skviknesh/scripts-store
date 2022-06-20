create table `searce-practice-data-analytics.mphhi_searce_stage.stg_medicare_spending_backup` as
select * from `searce-practice-data-analytics.mphhi_searce_stage.stg_medicare_spending`;

delete from `searce-practice-data-analytics.mphhi_searce_stage.stg_medicare_spending` where 1=1;

select * from `searce-practice-data-analytics.mphhi_searce_stage.stg_medicare_spending`;