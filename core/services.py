from django.shortcuts import get_object_or_404

class BaseService:
    model_class = None

    def prepare_data(self, validated_data):
        return validated_data

    def get_model_class(self):
        assert self.model_class is not None, (
                "%s should include model_class attribute or override get_model_class() method"
                % self.__class__.__name__
        )
        return self.model_class

    def create(self, validated_data, **kwargs):
        validated_data = self.prepare_data(validated_data)
        request = kwargs.pop("request")
        validated_data["user"] = request.user
        model_class = self.get_model_class()
        instance = model_class.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data, **kwargs):
        request = kwargs.get("request")
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def get(self, **kwargs):
        model_class = self.get_model_class()
        instance = get_object_or_404(model_class, **kwargs)
        return instance

    def update_status(self, instance, validated_data, **kwargs):
        request = kwargs.get("request")
        instance.is_active = validated_data['is_active']
        instance.save()
        return instance

    def all(self, **kwargs):
        model_class = self.get_model_class()
        instances = model_class.objects.filter(**kwargs)
        return instances
