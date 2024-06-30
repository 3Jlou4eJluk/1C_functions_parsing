# Generated from BSLMethodDescriptionParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BSLMethodDescriptionParser import BSLMethodDescriptionParser
else:
    from BSLMethodDescriptionParser import BSLMethodDescriptionParser

# This class defines a complete generic visitor for a parse tree produced by BSLMethodDescriptionParser.

class BSLMethodDescriptionParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BSLMethodDescriptionParser#methodDescription.
    def visitMethodDescription(self, ctx:BSLMethodDescriptionParser.MethodDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#deprecate.
    def visitDeprecate(self, ctx:BSLMethodDescriptionParser.DeprecateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#deprecateDescription.
    def visitDeprecateDescription(self, ctx:BSLMethodDescriptionParser.DeprecateDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#descriptionBlock.
    def visitDescriptionBlock(self, ctx:BSLMethodDescriptionParser.DescriptionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#description.
    def visitDescription(self, ctx:BSLMethodDescriptionParser.DescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#descriptionString.
    def visitDescriptionString(self, ctx:BSLMethodDescriptionParser.DescriptionStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#examples.
    def visitExamples(self, ctx:BSLMethodDescriptionParser.ExamplesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#examplesString.
    def visitExamplesString(self, ctx:BSLMethodDescriptionParser.ExamplesStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#callOptions.
    def visitCallOptions(self, ctx:BSLMethodDescriptionParser.CallOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#callOptionsString.
    def visitCallOptionsString(self, ctx:BSLMethodDescriptionParser.CallOptionsStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#parameters.
    def visitParameters(self, ctx:BSLMethodDescriptionParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#parameterString.
    def visitParameterString(self, ctx:BSLMethodDescriptionParser.ParameterStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#parameter.
    def visitParameter(self, ctx:BSLMethodDescriptionParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#subParameter.
    def visitSubParameter(self, ctx:BSLMethodDescriptionParser.SubParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#parameterName.
    def visitParameterName(self, ctx:BSLMethodDescriptionParser.ParameterNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#returnsValues.
    def visitReturnsValues(self, ctx:BSLMethodDescriptionParser.ReturnsValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#returnsValuesString.
    def visitReturnsValuesString(self, ctx:BSLMethodDescriptionParser.ReturnsValuesStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#returnsValue.
    def visitReturnsValue(self, ctx:BSLMethodDescriptionParser.ReturnsValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#typesBlock.
    def visitTypesBlock(self, ctx:BSLMethodDescriptionParser.TypesBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#typeDescription.
    def visitTypeDescription(self, ctx:BSLMethodDescriptionParser.TypeDescriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#type.
    def visitType(self, ctx:BSLMethodDescriptionParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#simpleType.
    def visitSimpleType(self, ctx:BSLMethodDescriptionParser.SimpleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#listTypes.
    def visitListTypes(self, ctx:BSLMethodDescriptionParser.ListTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#complexType.
    def visitComplexType(self, ctx:BSLMethodDescriptionParser.ComplexTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#hyperlinkType.
    def visitHyperlinkType(self, ctx:BSLMethodDescriptionParser.HyperlinkTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#spitter.
    def visitSpitter(self, ctx:BSLMethodDescriptionParser.SpitterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#hyperlinkBlock.
    def visitHyperlinkBlock(self, ctx:BSLMethodDescriptionParser.HyperlinkBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BSLMethodDescriptionParser#startPart.
    def visitStartPart(self, ctx:BSLMethodDescriptionParser.StartPartContext):
        return self.visitChildren(ctx)



del BSLMethodDescriptionParser