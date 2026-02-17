def build_logo_prompt(data: dict) -> str:
    """
    Builds an optimized logo generation prompt
    from collected user inputs.
    """

    prompt = f"""
    {data.get('style', '')} logo design for a {data.get('business_type', '')} company
    named {data.get('company_name', '')} in the {data.get('industry', '')} industry.
    Color palette: {data.get('colors', '')}.
    Typography: {data.get('font', '')}.
    Include icon elements related to: {data.get('icon', '')}.
    Tagline: {data.get('tagline', '')}.
    Flat vector style, minimal, clean, professional,
    centered composition, white background,
    high resolution, 1024x1024, flat vector style logo.
.
    """

    return prompt.strip()
