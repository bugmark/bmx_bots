require 'json'

basedir=File.expand_path("../", __dir__)

describe "all_rebuild" do
  describe "rebuild" do
    it "rebuilds the system" do
      result = `#{basedir}/rebuild`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["users"]).to          eq(1)
      expect(result["trackers"]).to          eq(0)
      expect(result["offers_open_bu"]).to eq(0)
      expect(result["offers_open_bf"]).to eq(0)
      expect(result["events"]).to         eq(2)
    end
  end

  describe "tracker_load" do
    it "loads trackers" do
      result = `#{basedir}/tracker_load`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["trackers"]).to  eq(1)
      expect(result["events"]).to eq(4)
    end
  end

  describe "user_load" do
    it "loads users" do
      result = `#{basedir}/user_load`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["users"]).to   eq(3)
      expect(result["events"]).to  eq(9)
    end
  end

  describe "simulation" do
    it "runs simulation" do
      result = `#{basedir}/simulation.py`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["users"]).to           eq(3)
      expect(result["trackers"]).to           eq(1)
      expect(result["issues"]).to          eq(2)
      expect(result["offers_open"]).to     eq(0)
      expect(result["contracts_open"]).to  eq(0)
      expect(result["events"]).to          eq(42)
    end

    it "has accurate user balances" do
      funder  = JSON.parse(`bmx user list --with_email=funder`).first
      workers = JSON.parse(`bmx user list --with_email=worker`)
      expect(funder["balance"]).to     eq(99800.0)
      expect(workers[0]["balance"]).to eq(10200.0)
    end
  end
end
