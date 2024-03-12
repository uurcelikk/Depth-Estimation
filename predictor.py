import torch
from PIL import Image
from misc import colorize

class DepthEstimationModel:
    def __init__(self, model):
        self.device = self._get_device()
        self.model = self._init_model(model).to(self.device)

    def _get_device(self):
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def _init_model(self, model_repo="isl-org/ZoeDepth", model_name="ZoeD_N"):
        torch.hub.help("intel-isl/MiDaS", "DPT_BEiT_L_384", force_reload=True)
        model = torch.hub.load(model_repo, model_name, pretrained=True, skip_validation=True)
        model.eval()
        print("Model initialized")
        return model

    def save_colored_depth(self, depth_numpy, out_path):
        colored = colorize(depth_numpy)
        Image.fromarray(colored).save(out_path)
        print('Image saved.')

    def calculate_depthmap(self, image_path, out_path):
        image = Image.open(image_path).convert("RGB")
        print('Image read')
        depth_numpy = self.model.infer_pil(image)
        self.save_colored_depth(depth_numpy, out_path)
        return f'Image saved at {out_path}'