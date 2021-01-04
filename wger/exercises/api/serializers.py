# -*- coding: utf-8 -*-

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

# Third Party
from rest_framework import serializers

# wger
from wger.exercises.models import (
    Equipment,
    Exercise,
    ExerciseBase,
    ExerciseCategory,
    ExerciseComment,
    ExerciseImage,
    Muscle
)


class ExerciseBaseSerializer(serializers.ModelSerializer):
    """
    Exercise serializer
    """
    class Meta:
        model = ExerciseBase
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    """
    Equipment serializer
    """
    class Meta:
        model = Equipment
        fields = '__all__'


class ExerciseImageSerializer(serializers.ModelSerializer):
    """
    ExerciseImage serializer
    """
    class Meta:
        model = ExerciseImage
        fields = '__all__'


class ExerciseCommentSerializer(serializers.ModelSerializer):
    """
    ExerciseComment serializer
    """
    class Meta:
        model = ExerciseComment
        fields = '__all__'


class ExerciseCategorySerializer(serializers.ModelSerializer):
    """
    ExerciseCategory serializer
    """
    class Meta:
        model = ExerciseCategory
        fields = '__all__'


class MuscleSerializer(serializers.ModelSerializer):
    """
    Muscle serializer
    """
    class Meta:
        model = Muscle
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    """
    Exercise serializer

    The fields from the new ExerciseBase are retrieved here as to retain
    compatibility with the old model where all the fields where in Exercise.
    """
    category = serializers.PrimaryKeyRelatedField(source='exercise_base.category',
                                                  read_only=True)
    muscles = serializers.PrimaryKeyRelatedField(source='exercise_base.muscles',
                                                 many=True,
                                                 read_only=True)
    muscles_secondary = serializers.PrimaryKeyRelatedField(source='exercise_base.muscles_secondary',
                                                           many=True,
                                                           read_only=True)
    equipment = serializers.PrimaryKeyRelatedField(source='exercise_base.equipment',
                                                   many=True,
                                                   read_only=True)

    class Meta:
        model = Exercise
        fields = ("id",
                  "uuid",
                  "name",
                  "description",
                  "creation_date",
                  "category",
                  "muscles",
                  "muscles_secondary",
                  "equipment",
                  "language",
                  "license",
                  "license_author")


class ExerciseInfoSerializer(serializers.ModelSerializer):
    """
    Exercise info serializer
    """

    images = ExerciseImageSerializer(source='exerciseimage_set', many=True)
    comments = ExerciseCommentSerializer(source='exercisecomment_set', many=True)
    category = ExerciseCategorySerializer(source='exercise_base.category')
    muscles = MuscleSerializer(source='exercise_base.muscles', many=True)
    muscles_secondary = MuscleSerializer(source='exercise_base.muscles_secondary', many=True)
    equipment = EquipmentSerializer(source='exercise_base.equipment', many=True)

    class Meta:
        model = Exercise
        depth = 1
        fields = ("id",
                  "name",
                  "uuid",
                  "description",
                  "creation_date",
                  "category",
                  "muscles",
                  "muscles_secondary",
                  "equipment",
                  "language",
                  "license",
                  "license_author",
                  "images",
                  "variations",
                  "comments")
