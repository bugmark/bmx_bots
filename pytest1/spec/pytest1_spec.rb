require 'json'

describe "all_rebuild" do
  describe "rebuild" do
    it "rebuilds the system" do
      result = `./pytest1/rebuild`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["num_users"]).to eq(1)
      expect(result["num_repos"]).to eq(0)
      expect(result["bu_offers"]).to eq(0)
      expect(result["bf_offers"]).to eq(0)
      expect(result["events"]).to    eq(2)
    end
  end

  describe "repo_load" do
    it "loads repos" do
      result = `./pytest1/repo_load`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["num_repos"]).to eq(1)
      expect(result["events"]).to eq(4)
    end
  end

  describe "user_load" do
    it "loads users" do
      result = `./pytest1/user_load`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["num_users"]).to eq(4)
      expect(result["events"]).to    eq(11)
    end
  end

  describe "simulation" do
    it "runs simulation" do
      result = `./pytest1/simru`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["num_users"]).to  eq(4)
      expect(result["num_repos"]).to  eq(1)
      expect(result["num_issues"]).to eq(4)
      expect(result["offers"]).to     eq(0)
      expect(result["contracts"]).to  eq(0)
      expect(result["events"]).to     eq(76)
    end

    it "has accurate user balances" do
      funder  = JSON.parse(`bmx user list --with_email=funder`).first
      workers = JSON.parse(`bmx user list --with_email=worker`)
      expect(funder["balance"]).to     eq(100400)
      expect(workers[0]["balance"]).to eq(9800)
      expect(workers[1]["balance"]).to eq(9800)
    end
  end
end
