require 'json'

base_dir=File.expand_path("../", __dir__)

# describe "all_rebuild" do
#   describe "clear" do
#     it "clears the system" do
#       result = `#{base_dir}/clear`
#       expect($?.exitstatus).to eq(0)
#       expect(result).to_not be_nil
#     end
#
#     it "generates accurate counts" do
#       result = JSON.parse(`bmx host counts`)
#       expect(result["users"]).to          eq(1)
#       expect(result["trackers"]).to          eq(0)
#       expect(result["offers_open_bf"]).to eq(0)
#       expect(result["offers_open_bf"]).to eq(0)
#       expect(result["events"]).to         eq(2)
#     end
#   end
#
#   describe "user_load" do
#     it "loads users" do #
#       result = `#{base_dir}/user_load.sh`
#       expect($?.exitstatus).to eq(0)
#       expect(result).to_not be_nil
#     end
#
#     it "generates accurate counts" do
#       result = JSON.parse(`bmx host counts`)
#       expect(result["users"]).to   eq(4)
#       expect(result["events"]).to  eq(9)
#     end
#   end
#
#   describe "tracker_load" do
#     it "loads trackers" do
#       result = `#{base_dir}/tracker_load`
#       expect($?.exitstatus).to eq(0)
#       expect(result).to_not be_nil
#     end
#
#     it "generates accurate counts" do
#       result = JSON.parse(`bmx host counts`)
#       expect(result["trackers"]).to  eq(3)
#       expect(result["issues"]).to eq(6)
#       expect(result["events"]).to eq(19)
#     end
#   end
#
#   describe "offer_load" do
#     it "loads bu" do
#       result = `#{base_dir}/offer_load`
#       expect($?.exitstatus).to eq(0)
#       expect(result).to_not be_nil
#     end
#
#     it "generates accurate counts" do
#       result = JSON.parse(`bmx host counts`)
#       expect(result["offers_open_bu"]).to eq(7)
#       expect(result["offers_open_bf"]).to eq(5)
#       expect(result["events"]).to         eq(32)
#     end
#   end
# end
