require 'json'

basedir=File.expand_path("../", __dir__)

describe "all_rebuild" do
  describe "clear" do
    it "clears the system" do
      result = `#{basedir}/clear`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["users"]).to          eq(1)
      expect(result["repos"]).to          eq(0)
      expect(result["offers_open_bu"]).to eq(0)
      expect(result["offers_open_bf"]).to eq(0)
      expect(result["events"]).to         eq(2)
    end
  end

  describe "user_load" do
    it "loads users" do
      result = `#{basedir}/user_load.sh`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["users"]).to     eq(4)
      expect(result["events"]).to    eq(9)
    end
  end

  describe "repo_load" do
    it "loads repos" do
      result = `#{basedir}/repo_load`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["repos"]).to  eq(3)
      expect(result["issues"]).to eq(6)
      expect(result["events"]).to eq(19)
    end
  end

  describe "offer_load" do
    it "loads bu" do
      result = `#{basedir}/offer_load`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end
  end
end
