def genai_advisor(course, predicted_score):
    advice = []

    if predicted_score < 5:
        advice.append("⚠️ Course has low success potential. Consider revising pricing and content depth.")

    if course["price_usd"] > 50:
        advice.append("💰 High pricing detected. Discounts or tiered pricing may improve enrollments.")

    if course["rating"] < 4:
        advice.append("⭐ Improve content quality to increase ratings and learner satisfaction.")

    if course["reviews_count"] < 50:
        advice.append("📝 Encourage learners to leave reviews to build credibility.")

    if course["difficulty_level"].lower() == "advanced":
        advice.append("🎯 Advanced courses perform better with clear prerequisites and project-based learning.")

    if predicted_score >= 8:
        advice.append("🚀 Strong performance! Consider adding certifications or advanced modules.")

    return advice
