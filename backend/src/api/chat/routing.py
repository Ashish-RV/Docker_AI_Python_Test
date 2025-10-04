from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from api.db import get_session
import os
from typing import List
from .models import ChatMessagePayload, ChatMessage,ChatMessageListItem

router = APIRouter()

MY_PROJECT = os.environ.get("MY_PROJECT")
@router.get("/")
def Chat_health():
    return {"hello":"Chat", "Project Name": MY_PROJECT}

@router.get("/recent/", response_model=List[ChatMessageListItem])
def chat_list_messages(session: Session=Depends(get_session)):
    query = select(ChatMessage)
    result = session.exec(query).fetchall()[:10]
    return result

# curl -X POST -d '{"message":"hello world"}' -H "Content-Type:application/json" http://localhost:8080/api/chats/
@router.post("/", response_model=List[ChatMessageListItem])
def chat_create_message(payload: ChatMessagePayload, session: Session=Depends(get_session)):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj