import os
import shutil

if __name__ == '__main__':

    for singer_file in os.listdir("data_svc/singer"):
        if singer_file.endswith("spk.npy"):
            singler = singer_file.replace(".spk.npy", "")
            os.makedirs(os.path.join("models", singler), exist_ok=True)
            shutil.copy(os.path.join("data_svc", "singer", singer_file), os.path.join("models", singler, "speaker0.spk.npy"))
            shutil.copy("sovits5.0.pth", os.path.join("models", singler))