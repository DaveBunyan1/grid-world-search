from fastapi.testclient import TestClient

from grid_search.api.app import app

client = TestClient(app)


def test_get_algorithms():

    response = client.get("/algorithms")

    assert response.status_code == 200

    assert response.json() == [
        "bfs",
        "dfs",
        "dijkstra",
        "astar",
    ]


def test_generate_grid():

    response = client.post(
        "/generate-grid",
        json={
            "rows": 5,
            "cols": 5,
            "obstacle_probability": 0.0,
            "seed": 42,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data["grid"]["cells"]) == 5
    assert len(data["grid"]["cells"][0]) == 5

    assert data["grid"]["cells"][0][0]["blocked"] is False
    assert data["grid"]["cells"][4][4]["blocked"] is False


def test_search_bfs():

    response = client.post(
        "/search",
        json={
            "algorithm": "bfs",
            "grid": {
                "cells": [
                    [
                        {"blocked": False, "cost": 1},
                        {"blocked": False, "cost": 1},
                    ],
                    [
                        {"blocked": False, "cost": 1},
                        {"blocked": False, "cost": 1},
                    ],
                ]
            },
            "start": {
                "row": 0,
                "col": 0,
            },
            "goal": {
                "row": 1,
                "col": 1,
            },
        },
    )

    assert response.status_code == 200

    result = response.json()

    assert result["path_found"] is True
    assert result["path_length"] == 3
    assert result["nodes_expanded"] > 0
