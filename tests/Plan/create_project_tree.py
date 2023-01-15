import os


def create_project_tree():
    project_root = "project"
    dirs = [
        "app/games/guessgame",
        "app/games/memorygame",
        "app/scores",
        "app/static/css",
        "app/static/js",
        "app/static/img",
        "app/templates",
        "tests/games",
        "tests/scores",
        "docker",
        "helm"
    ]

    for dir in dirs:
        os.makedirs(os.path.join(project_root, dir), exist_ok=True)

    with open(os.path.join(project_root, "../../app/games/guessgame", "__init__.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/games/guessgame", "views.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/games/guessgame", "models.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/games/guessgame", "urls.py"), "w") as f:
        pass
    os.makedirs(os.path.join(project_root, "../../app/games/guessgame/templates"), exist_ok=True)
    with open(os.path.join(project_root, "../../app/games/guessgame/templates", "guessgame.html"), "w") as f:
        pass

    with open(os.path.join(project_root, "../../app/games/memorygame", "__init__.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/games/memorygame", "views.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/games/memorygame", "models.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/games/memorygame", "urls.py"), "w") as f:
        pass
    os.makedirs(os.path.join(project_root, "../../app/games/memorygame/templates"), exist_ok=True)
    with open(os.path.join(project_root, "../../app/games/memorygame/templates", "memorygame.html"), "w") as f:
        pass

    with open(os.path.join(project_root, "../../app/scores", "__init__.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/scores", "views.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/scores", "models.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/scores", "urls.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/scores", "Score.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/scores", "database.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/__init__.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/urls.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/views.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/models.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/templates", "base.html"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/templates", "gamepicker.html"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../app/templates", "introduction.html"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../manage.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../requirements.txt"), "w") as f:
        pass
    with open(os.path.join(project_root, "../games/test_guessgame.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../games/test_memorygame.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../scores/test_scores.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../scores/test_database.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../test_end_to_end.py"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../docker/Dockerfile"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../docker/docker-compose.yml"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../helm/Chart.yaml"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../helm/values.yaml"), "w") as f:
        pass
    os.makedirs(os.path.join(project_root, "../../helm/templates"), exist_ok=True)
    with open(os.path.join(project_root, "../../helm/templates/deployment.yaml"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../helm/templates/service.yaml"), "w") as f:
        pass
    with open(os.path.join(project_root, "../../README.md"), "w") as f:
        pass

if __name__ == "__main__":
    create_project_tree()





