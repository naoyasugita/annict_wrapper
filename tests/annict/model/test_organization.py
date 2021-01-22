import pytest
from annict.model.organization import Organization
from annict.model.organization import Organizations


class TestOrganizationModel:
    def test_to_dict(self, fixture_organization):
        actual = fixture_organization["organization_dict"]

        organization = fixture_organization["organization"]
        excepted = organization.to_dict()

        assert actual == excepted

    def test_from_dict(self, fixture_organization):
        actual = fixture_organization["organization"]

        organization_dict = fixture_organization["organization_dict"]
        excepted = Organization.from_dict(organization_dict)

        assert actual == excepted


class TestOrganizationsModel:
    def test_organizations_append_when_type_ok(self, fixture_organization):
        organizations = Organizations()
        organization = fixture_organization["organization"]
        organization_2 = fixture_organization["organization"]
        organizations.append(organization)
        organizations.append(organization_2)
        excepted = len(organizations._list)

        actual = 2

        assert actual == excepted

    def test_organizations_append_when_type_error(self):
        organizations = Organizations()
        with pytest.raises(TypeError):
            organizations.append("dammy")

    def test_organizations_to_dict(self, fixture_organization):
        organizations = Organizations()
        org = fixture_organization["organization"]
        organizations.append(org)
        excepted = organizations.to_dict()

        organization_dict = fixture_organization["organization_dict"]
        actual = [organization_dict]

        assert actual == excepted
