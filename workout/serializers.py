from rest_framework import serializers

from workout_exercise.models import Workout_exercise
from .models import Workout
from workout_exercise.serializers import Workout_exerciseSerializer
from exercise.models import Exercise


class WorkoutSerializer(serializers.ModelSerializer):
    exercises = Workout_exerciseSerializer(many=True)

    def create(self, validated_data):
        exercises = validated_data.pop("exercises")

        workout_obj = Workout.objects.create(**validated_data)

        for exercise in exercises:
            title = exercise.pop("exercise")
            exercise_obj, created = Exercise.objects.get_or_create(title=title["title"])

            Workout_exercise.objects.create(
                **exercise, workout=workout_obj, exercise=exercise_obj
            )

        return workout_obj

    def update(self, instance, validated_data):
        exercises = validated_data.pop("exercises", None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if exercises is not None:
            old_exercises = instance.exercises.all()
            old_exercises.delete()

            for exercise in exercises:
                title = exercise.pop("exercise")
                exercise_obj, created = Exercise.objects.get_or_create(
                    title=title["title"]
                )

                Workout_exercise.objects.create(
                    **exercise, workout=instance, exercise=exercise_obj
                )
        instance.save()
        return instance

    class Meta:
        model = Workout
        fields = [
            "id",
            "muscle_group",
            "day",
            "title",
            "description",
            "exercises",
        ]
        read_only_fields = [
            "id",
            "sheet",
            "exercises",
        ]


# class WorkoutSerializer(serializers.Serializer):
#     id = serializers.UUIDField(read_only=True)
#     muscle_group = serializers.CharField(max_length=10)
#     day = serializers.CharField(max_length=10)
#     title = serializers.CharField(max_length=120, )
#     description =
#     exercises = Workout_exerciseSerializer(many=True)

#     def create(self, validated_data):
#         exercises = validated_data.pop("exercises")

#         workout_obj = Workout.objects.create(**validated_data)

#         for exercise in exercises:
#             title = exercise.pop("exercise_title")
#             exercise_obj = Exercise.objects.create(title=title)

#             Workout_exercise.objects.create(
#                 **exercise, workout=workout_obj, exercise=exercise_obj
#             )

#         return workout_obj

#     class Meta:
#         model = Workout
#         fields = [
#             "id",
#             "muscle_group",
#             "day",
#             "title",
#             "description",
#             "exercises",
#         ]
#         read_only_fields = [
#             "id",
#             "sheet",
#             "exercises",
#         ]
