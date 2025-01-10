from pipeline.data_loader import DataLoader
from pipeline.model import Model
from blender.render import Renderer

def main():
    # Load and preprocess the data
    data_loader = DataLoader()
    images = data_loader.load_images()

    # Initialize the model and generate 3D models
    model = Model()
    generated_models = model.generate(images)

    # Render the generated models
    renderer = Renderer()
    for model in generated_models:
        renderer.render(model)

if __name__ == "__main__":
    main()