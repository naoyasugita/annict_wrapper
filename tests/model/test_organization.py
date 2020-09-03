import pytest

from annict_wrapper.model.organization import Organization
from annict_wrapper.model.organization import Organizations


class TestOrganizationModel:
    def test_to_dict(self, fixture_organization):
        organization_dict = fixture_organization["organization_dict"]
        assert Organization(**organization_dict).to_dict() == organization_dict


class TestOrganizationsModel:
    def test_organizations_append_when_type_ok(self, fixture_organization):
        organizations = Organizations()
        organization = fixture_organization["organization"]
        organization_2 = fixture_organization["organization"]
        organizations.append(organization)
        organizations.append(organization_2)
        assert len(organizations._list) == 2

    def test_organizations_append_when_type_error(self):
        organizations = Organizations()
        with pytest.raises(TypeError):
            organizations.append("dammy")

    def test_organizations_to_dict(self, fixture_organization):
        organizations = Organizations()
        org = fixture_organization["organization"]
        organization_dict = fixture_organization["organization_dict"]
        organizations.append(org)
        assert organizations.to_dict() == [organization_dict]
