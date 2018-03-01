require 'json'

describe "rebuild" do
  describe "clear" do
    it "clears the system" do
      result = `./rebuild/clear`
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
      result = `./rebuild/user_load`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["users"]).to   eq(6)
      expect(result["events"]).to  eq(13)
    end
  end

  describe "repo_load" do
    it "loads repos" do
      result = `./rebuild/repo_load Test`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["repos"]).to  eq(1)
      expect(result["issues"]).to eq(13)
      expect(result["events"]).to eq(28)
    end
  end

  describe "offer_load" do
    it "loads bu" do
      result = `./rebuild/offer_load`
      expect($?.exitstatus).to eq(0)
      expect(result).to_not be_nil
    end

    it "generates accurate counts" do
      result = JSON.parse(`bmx host counts`)
      expect(result["offers_open_bu"]).to eq(7)
      expect(result["offers_open_bf"]).to eq(5)
      expect(result["events"]).to         eq(41)
    end
  end
end
