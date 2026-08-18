from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# This defines the structure for how i want the model to return responses
class JobPosting(BaseModel):
    company: str
    role: str
    requirements: list[str]

def parse_job_posting(job_posting_text: str):
    response = client.responses.parse(
        model="gpt-4o-2024-08-06",
        input=[
            {"role": "system", "content": "Extract the company name, role, and key requirements from this job posting."},
            {"role": "user", "content": job_posting_text}
        ],
        text_format=JobPosting,
    )
    return response.output_parsed

if __name__ == "__main__":
    sample_posting = """
About Terminal
Terminal builds telematics data infrastructure for the commercial fleet industry. Commercial auto insurers and fleet software companies, including industry leaders like Intact Insurance, depend on our platform to access GPS, speeding, and vehicle data from 330+ telematics providers. We recently raised our Series A led by Battery Ventures and are backed by Y Combinator, Golden Ventures, Penske Transportation Solutions, and Intact Private Capital. Our team works together in person in Toronto, combining early-stage speed with late-stage maturity while processing many terabytes of vehicle data every day.

For more on working at Terminal, see our careers page at withterminal.com/careers.

Note that this role is only open to Toronto/GTA-based candidates.

About the role
This role spans everything our customers touch: the integrations that turn raw vehicle telematics from 330+ providers into clean data, the public APIs enterprises build against, the dashboards they work in, and the ingestion platform underneath it all. It is a mix of product and backend engineering, shaping the APIs and deeper backend components our customers depend on. If you want to be three layers of abstraction from the customer, this isn't the role for you.

You'll own systems end-to-end and help shape the product, not just build it. Working closely with customers, you'll turn their problems into the right abstractions and reusable components that scale. Your judgment directly shapes how customers launch products on high-volume telematics data to benefit vehicles and fleets on the road every day.

What you'll do
Design new features and platform capabilities, partnering with teammates and customers to expand what Terminal can do.

Build the primitives that power our platform: connector frameworks, orchestration, monitoring, auth, testing, and more.

Shape how we build, not just what we build: the AI-powered tooling that lets the platform increasingly improve itself.

Add and maintain integrations across 330+ telematics providers, making messy, under-documented APIs reliable.

Work with integration partners to shape their APIs, expand the data we can offer, and improve performance at the source.

Work directly with customers: demos, implementations, and troubleshooting threads.

Work day to day in TypeScript/Node.js to deploy services on AWS.

What we're looking for
A strong backend engineer who's shipped and owned production systems end to end.

Can be trusted with hard architecture decisions.

Thrives against messy, undocumented, uncooperative external systems and makes them reliable anyway.

Depth in distributed systems: you anticipate failures and can debug fast when things break.

Platform builder: you make the systems other teams stand on, and design them to last.

Sound judgment in ambiguity: you scope before building and know when to go deep on details VS ship fast experiments.

Customer-facing: you want to be in the demo, the implementation call, and the hard troubleshooting thread so you can learn more about our customers.

Strong in Node.js and TypeScript, or confident to pick it up fast.

You don't need to check every box. If you're missing some but confident you'll close the gap quickly, apply anyway.

Nice to have
Serverless and event-driven architectures (Lambda, SQS, Kafka, EventBridge).

Orchestration and workflow engines (Step Functions, Temporal).

JVM languages for cross-team work with the data platform.

How we work
In person 4 days/week, downtown Toronto. We build better together in a room.

High ownership. Everyone takes projects end-to-end and helps shape the product.

Platform thinking. Our work is the foundation on which other teams build their products. We design capabilities that compose into features and accept complexity so others don't have to.

Talk to customers. Whether it's a paying customer or an internal team, we talk to our customers to understand their problems before we ship solutions.

 
Compensation
We hire for this role at two levels and calibrate to where you come in. All compensation is base salary plus meaningful equity.

Senior: base $185,000 to $230,000 + equity

Staff: base $220,000 to $285,000 + equity

Benefits
Strong compensation and equity packages.

Brand new MacBook and computer equipment.

Top-tier health/dental benefits and a flexible healthcare spending account.

Personal spending account for professional development, fitness and wellness.

Four weeks paid time off + statutory holidays.

In-person culture with an office located in downtown Toronto.

The interview process
Intro call with the CTO (30 min)

Virtual system design (60 min)

On-site technical loop (120 min)

On-site culture loop + final (180 min)

Accessibility and accommodation

Terminal is committed to an accessible hiring process. If you need an accommodation at any stage — applying, interviewing, or completing an assessment — email careers@withterminal.com and we will work with you to meet your needs. Accommodations are available under the Accessibility for Ontarians with Disabilities Act (AODA) and the Ontario Human Rights Code, and requesting one will never affect how your application is considered."""
    result = parse_job_posting(sample_posting)
    print(result)