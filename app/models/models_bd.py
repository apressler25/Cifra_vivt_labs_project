
from sqlalchemy import (
    BigInteger, String, Boolean, Date, DateTime, SmallInteger, 
    LargeBinary, Text, ForeignKey, DateTime, func
)
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from typing import Optional
from datetime import datetime, date

class Base(DeclarativeBase):
    pass

class TargetMuscleCategory(Base):
    __tablename__ = 'Target_muscle_category'
    
    id_muscle_category: Mapped[int] = mapped_column(SmallInteger, primary_key=True)
    name_muscle_category: Mapped[str] = mapped_column(String(255))
    
    # Relationships
    workout_exercises: Mapped[list['WorkoutExercises']] = relationship(back_populates='muscle_category')

class User(Base):
    __tablename__ = 'User'
    
    id_user: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_telegram: Mapped[int] = mapped_column(BigInteger)
    name_user: Mapped[str] = mapped_column(String(255))
    date_registration_user: Mapped[datetime] = mapped_column(DateTime(timezone=False), default=datetime.now) #если не передавать значение, устанавливается текущее время
    info_restrictions_user: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    sub_user: Mapped[bool] = mapped_column(Boolean, default=False)
    
    # Relationships
    programs_workout: Mapped[list['ProgramsWorkout']] = relationship(back_populates='user')
    restrictions: Mapped[list['Restrictions']] = relationship(back_populates='user')

class WorkoutExercises(Base):
    __tablename__ = 'Workout_exercises'
    
    id_workout_exercises: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name_workout_exercises: Mapped[str] = mapped_column(String(255))
    id_creation_user: Mapped[str] = mapped_column(String(255))
    notice_workout_exercises: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    id_muscle_category: Mapped[int] = mapped_column(SmallInteger, ForeignKey('Target_muscle_category.id_muscle_category'))
    gif_file_workout_exercises: Mapped[Optional[bytes]] = mapped_column(LargeBinary, nullable=True)
    
    # Relationships
    muscle_category: Mapped['TargetMuscleCategory'] = relationship(back_populates='workout_exercises')
    workout_ex_pool: Mapped[list['WorkoutExPool']] = relationship(back_populates='workout_exercise')
    restrictions: Mapped[list['Restrictions']] = relationship(back_populates='workout_exercise')

class ProgramsWorkout(Base):
    __tablename__ = 'Programs_workout'
    
    id_programs_workout: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name_programs_workout: Mapped[str] = mapped_column(String(255))
    id_user: Mapped[int] = mapped_column(BigInteger, ForeignKey('User.id_user'))
    week_day_programs_workout: Mapped[str] = mapped_column(String(255))
    
    # Relationships
    user: Mapped['User'] = relationship(back_populates='programs_workout')
    workout_ex_pool: Mapped[list['WorkoutExPool']] = relationship(back_populates='program')

class WorkoutExPool(Base):
    __tablename__ = 'Workout_ex_pool'
    
    id_ex_pool: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_programs_workout: Mapped[int] = mapped_column(BigInteger, ForeignKey('Programs_workout.id_programs_workout'))
    id_workout_exercises: Mapped[int] = mapped_column(BigInteger, ForeignKey('Workout_exercises.id_workout_exercises'))
    max_target_iteration_ex_pool: Mapped[int] = mapped_column(SmallInteger)
    min_target_iteration_ex_pool: Mapped[int] = mapped_column(SmallInteger)
    approaches_target_ex_pool: Mapped[int] = mapped_column(SmallInteger)
    weight_ex_pool: Mapped[int] = mapped_column(SmallInteger)
    
    # Relationships
    program: Mapped['ProgramsWorkout'] = relationship(back_populates='workout_ex_pool')
    workout_exercise: Mapped['WorkoutExercises'] = relationship(back_populates='workout_ex_pool')
    train_pools: Mapped[list['TrainPool']] = relationship(back_populates='exercise_pool')

class TrainInfo(Base):
    __tablename__ = 'Train_info'
    
    id_train_info: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    datetime_start_train_info: Mapped[datetime] = mapped_column(DateTime(timezone=False))
    datetime_end_train_info: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False), nullable=True)
    check_train_info: Mapped[bool] = mapped_column(Boolean)
    
    # Relationships
    train_pools: Mapped[list['TrainPool']] = relationship(back_populates='train_info')

class TrainPool(Base):
    __tablename__ = 'Train_pool'
    
    id_train_pool: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_train_info: Mapped[int] = mapped_column(BigInteger, ForeignKey('Train_info.id_train_info'))
    id_ex_pool: Mapped[int] = mapped_column(BigInteger, ForeignKey('Workout_ex_pool.id_ex_pool'))
    record_bool: Mapped[bool] = mapped_column(Boolean)
    
    # Relationships
    train_info: Mapped['TrainInfo'] = relationship(back_populates='train_pools')
    exercise_pool: Mapped['WorkoutExPool'] = relationship(back_populates='train_pools')
    approaches_records: Mapped[list['ApproachesRec']] = relationship(back_populates='train_pool')

class ApproachesRec(Base):
    __tablename__ = 'Approaches_rec'
    
    id_approaches_rec: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    weight_approaches_rec: Mapped[int] = mapped_column(BigInteger)
    rest_time_up_approaches_rec: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=False), nullable=True)
    rest_time_num_approaches_rec: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    num_iteration_approaches_rec: Mapped[int] = mapped_column(SmallInteger)
    id_train_pool: Mapped[int] = mapped_column(BigInteger, ForeignKey('Train_pool.id_train_pool'))
    
    # Relationships
    train_pool: Mapped['TrainPool'] = relationship(back_populates='approaches_records')

class Restrictions(Base):
    __tablename__ = 'Restrictions'
    
    id_restrictions: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_workout_exercises: Mapped[int] = mapped_column(BigInteger, ForeignKey('Workout_exercises.id_workout_exercises'))
    id_user: Mapped[int] = mapped_column(BigInteger, ForeignKey('User.id_user'))
    
    # Relationships
    workout_exercise: Mapped['WorkoutExercises'] = relationship(back_populates='restrictions')
    user: Mapped['User'] = relationship(back_populates='restrictions')



