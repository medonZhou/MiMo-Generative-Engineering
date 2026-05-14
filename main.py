from fastapi import FastAPI, HTTPException, BackgroundTasks
from models.schemas import CADAssemblyData, EngineeringReport
from core.orchestrator import GenerativeWorkflow
import uuid

app = FastAPI(
    title="MiMo Generative Engineering API",
    description="AI-Native Automotive Structural Design Platform",
    version="1.0.0"
)

@app.post("/api/v1/audit-assembly", response_model=EngineeringReport)
async def audit_cad_assembly(cad_data: CADAssemblyData):
    """
    接收前端或 CAD 插件传递的装配体元数据，触发多智能体审查工作流。
    """
    if not cad_data.stp_file_hash:
        raise HTTPException(status_code=400, detail="Invalid STP file integrity.")
        
    trace_id = f"REQ-{uuid.uuid4().hex[:8].upper()}"
    workflow = GenerativeWorkflow(trace_id=trace_id)
    
    # 执行长链推理工作流
    report = await workflow.execute_design_audit(cad_data)
    return report

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
