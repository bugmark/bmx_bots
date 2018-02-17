# SPDX-License-Identifier: MPL-2.0

require 'json'

describe "all_rebuild" do
  describe "clear" do
    it "clears the system" do
      result = `./forecast1/clear`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["num_users"]).to eq(1)
      expect(result["num_repos"]).to eq(0)
      expect(result["bu_offers"]).to eq(0)
      expect(result["bf_offers"]).to eq(0)
      expect(result["events"]).to    eq(1)
    end
  end

  describe "user_load" do
    it "loads users" do
      result = `./forecast1/user_load.sh`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["num_users"]).to eq(4)
      expect(result["events"]).to    eq(7)
    end
  end

  describe "repo_load" do
    it "loads repos" do
      result = `./forecast1/repo_load`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["num_repos"]).to eq(3)
      expect(result["num_issues"]).to eq(6)
      expect(result["events"]).to eq(16)
    end
  end

  describe "offer_load" do
    it "loads bu" do
      result = `./forecast1/offer_load`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["bu_offers"]).to eq(7)
      expect(result["bf_offers"]).to eq(5)
      expect(result["events"]).to eq(28)
    end
  end
end
