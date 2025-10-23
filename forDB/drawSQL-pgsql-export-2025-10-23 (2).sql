CREATE TABLE "Workout_exercises"(
    "id_workout_exercises" BIGINT NOT NULL,
    "name_workout_exercises" VARCHAR(255) NOT NULL,
    "id_creation_user" BIGINT NOT NULL,
    "notice_workout_exercises" VARCHAR(255) NULL,
    "id_muscle_category" SMALLINT NOT NULL,
    "gif_file_workout_exercises" bytea NULL,
    "vision_user" BOOLEAN NOT NULL
);
ALTER TABLE
    "Workout_exercises" ADD PRIMARY KEY("id_workout_exercises");
CREATE TABLE "User"(
    "id_telegram" BIGINT NOT NULL,
    "name_user" VARCHAR(255) NOT NULL,
    "date_registration_user" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "info_restrictions_user" VARCHAR(255) NULL,
    "sub_user" BOOLEAN NOT NULL
);
ALTER TABLE
    "User" ADD PRIMARY KEY("id_telegram");
CREATE TABLE "Train_pool"(
    "id_train_pool" BIGINT NOT NULL,
    "id_train_info" BIGINT NOT NULL,
    "record_bool" BOOLEAN NOT NULL,
    "id_workout_exercises" BIGINT NOT NULL
);
ALTER TABLE
    "Train_pool" ADD PRIMARY KEY("id_train_pool");
CREATE TABLE "Programs_workout"(
    "id_programs_workout" BIGINT NOT NULL,
    "name_programs_workout" VARCHAR(255) NOT NULL,
    "id_user" BIGINT NOT NULL,
    "week_day_programs_workout" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Programs_workout" ADD PRIMARY KEY("id_programs_workout");
CREATE TABLE "Workout_ex_pool"(
    "id_ex_pool" BIGINT NOT NULL,
    "id_programs_workout" BIGINT NOT NULL,
    "id_workout_exercises" BIGINT NOT NULL,
    "max_target_iteration_ex_pool" SMALLINT NOT NULL,
    "min_target_iteration_ex_pool" SMALLINT NOT NULL,
    "approaches_target_ex_pool" SMALLINT NOT NULL,
    "weight_ex_pool" SMALLINT NOT NULL
);
ALTER TABLE
    "Workout_ex_pool" ADD PRIMARY KEY("id_ex_pool");
CREATE TABLE "Target_muscle_category"(
    "id_muscle_category" SMALLINT NOT NULL,
    "name_muscle_category" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Target_muscle_category" ADD PRIMARY KEY("id_muscle_category");
CREATE TABLE "Train_info"(
    "id_train_info" BIGINT NOT NULL,
    "datetime_start_train_info" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "datetime_end_train_info" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "check_train_info" BOOLEAN NOT NULL,
    "Id_user" BIGINT NOT NULL,
    "name_programs_workout" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "Train_info" ADD PRIMARY KEY("id_train_info");
CREATE TABLE "Approaches_rec"(
    "id_approaches_rec" BIGINT NOT NULL,
    "weight_approaches_rec" BIGINT NOT NULL,
    "rest_time_up_approaches_rec" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "rest_time_down_approaches_rec" TIMESTAMP(0) WITHOUT TIME ZONE NULL,
    "num_iteration_approaches_rec" SMALLINT NOT NULL,
    "id_train_pool" BIGINT NOT NULL
);
ALTER TABLE
    "Approaches_rec" ADD PRIMARY KEY("id_approaches_rec");
CREATE TABLE "Restrictions"(
    "id_restrictions" BIGINT NOT NULL,
    "id_workout_exercises" BIGINT NOT NULL,
    "id_user" BIGINT NOT NULL
);
ALTER TABLE
    "Restrictions" ADD PRIMARY KEY("id_restrictions");
ALTER TABLE
    "Workout_ex_pool" ADD CONSTRAINT "workout_ex_pool_id_workout_exercises_foreign" FOREIGN KEY("id_workout_exercises") REFERENCES "Workout_exercises"("id_workout_exercises");
ALTER TABLE
    "Train_info" ADD CONSTRAINT "train_info_id_user_foreign" FOREIGN KEY("Id_user") REFERENCES "User"("id_telegram");
ALTER TABLE
    "Workout_exercises" ADD CONSTRAINT "workout_exercises_id_muscle_category_foreign" FOREIGN KEY("id_muscle_category") REFERENCES "Target_muscle_category"("id_muscle_category");
ALTER TABLE
    "Programs_workout" ADD CONSTRAINT "programs_workout_id_user_foreign" FOREIGN KEY("id_user") REFERENCES "User"("id_telegram");
ALTER TABLE
    "Train_pool" ADD CONSTRAINT "train_pool_id_workout_exercises_foreign" FOREIGN KEY("id_workout_exercises") REFERENCES "Workout_exercises"("id_workout_exercises");
ALTER TABLE
    "Restrictions" ADD CONSTRAINT "restrictions_id_user_foreign" FOREIGN KEY("id_user") REFERENCES "User"("id_telegram");
ALTER TABLE
    "Approaches_rec" ADD CONSTRAINT "approaches_rec_id_train_pool_foreign" FOREIGN KEY("id_train_pool") REFERENCES "Train_pool"("id_train_pool");
ALTER TABLE
    "Train_pool" ADD CONSTRAINT "train_pool_id_train_info_foreign" FOREIGN KEY("id_train_info") REFERENCES "Train_info"("id_train_info");
ALTER TABLE
    "Workout_ex_pool" ADD CONSTRAINT "workout_ex_pool_id_programs_workout_foreign" FOREIGN KEY("id_programs_workout") REFERENCES "Programs_workout"("id_programs_workout");
ALTER TABLE
    "Restrictions" ADD CONSTRAINT "restrictions_id_workout_exercises_foreign" FOREIGN KEY("id_workout_exercises") REFERENCES "Workout_exercises"("id_workout_exercises");