import graphene
from graphene_django import DjangoObjectType

from .models import Occupation


class OccupationType(DjangoObjectType):
    class Meta:
        model = Occupation
        fields = ('id', 'name', 'company_name', 'position_name',
                  'hire_date', 'fire_date', 'salary',
                  'fraction', 'base', 'advance', 'by_hours')


class Query(graphene.ObjectType):
    get_occupations = graphene.List(OccupationType)
    get_occupation = graphene.Field(OccupationType, occupationid=graphene.Int(required=True))

    # Возвращает все все Occupations
    def resolve_get_occupations(root, info):
        return Occupation.objects.all()

    def resolve_get_occupation(root, info, occupationid):
        try:
            return Occupation.objects.get(id=occupationid)
        except Occupation.DoesNotExist:
            return None


class OccupationMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        companyName = graphene.String(required=True)  # companyName: String!,
        positionName = graphene.String(required=True)  # positionName: String!,
        hireDate = graphene.Date(required=True)  # hireDate: Date!,
        fireDate = graphene.Date()  # fireDate: Date,
        salary = graphene.Int(required=True)  # salary: Int!,
        fraction = graphene.Int(required=True)  # fraction: Int!,
        base = graphene.Int(required=True)  # base: Int!,
        advance = graphene.Int(required=True)  # advance: Int!,
        by_hours = graphene.Boolean(required=True)  # by_hours: Boolean!

    # Ответ
    occupation = graphene.Field(OccupationType)

    def mutate(self, info,
               name, companyName, positionName, hireDate, fireDate, salary, fraction, base, advance, by_hours):
        occupation = Occupation.objects.create(
            name=name,
            company_name=companyName,
            position_name=positionName,
            hire_date=hireDate,
            fire_date=fireDate,
            salary=salary,
            fraction=fraction,
            base=base,
            advance=advance,
            by_hours=by_hours
        )
        occupation.save()
        return OccupationMutation(occupation=occupation)


class Mutation(graphene.ObjectType):
    add_occupation = OccupationMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
