from flask import Blueprint

from app.api.bills import Bills


api_bp = Blueprint("api_bp", __name__, url_prefix="/api")









