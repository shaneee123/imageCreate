from fastapi import FastAPI, HTTPException
import openai
from fastapi.responses import JSONResponse

# FastAPI 애플리케이션 생성
app = FastAPI()

# OpenAI API 키 설정
openai.api_key = ""  # 실제 API 키를 여기에 넣어주세요

# 이미지 생성 엔드포인트
@app.get("/generate-image")
async def generate_image():
    try:
        # OpenAI DALL·E 3 API를 호출하여 이미지 생성
        response = openai.Image.create(
            prompt="A desperate zombie with a ravenous hunger, depicted in a fantasy movie setting. The scene is dark and eerie, emphasizing the fantasy atmosphere. The zombie's expression and posture clearly convey its desperation to eat.",
            size="1024x1024",
            n=1,
        )

        # 응답에서 이미지 URL 추출
        image_url = response['data'][0]['url']
        
        # 이미지 URL을 JSON 형식으로 반환
        return JSONResponse(content={"imageUrl": image_url})
    
    except Exception as e:
        # 이미지 생성 실패 시 에러 메시지 반환
        raise HTTPException(status_code=500, detail=str(e))